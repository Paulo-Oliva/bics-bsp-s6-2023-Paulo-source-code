#!/bin/bash

MODEL=$1
FOLDER=$2

if [ -z "$MODEL" ] || [ -z "$FOLDER" ]; then
	echo "Usage: $0 <model> <folder>"
	exit 1
fi

# Get the current date
cur_date=$(date +'%Y-%m-%d_%H-%M-%S')

# for each folder in the FID directory sorted numerically
for folder in $(ls -v "$FOLDER"); do
	echo "$folder"
	fid_score=$(python -m pytorch_fid --device cuda:0 "$MODEL" "$FOLDER"/"$folder")
	echo "$fid_score"
	# Append the folder name and the FID score to a file
	{
		echo "$folder"
		echo "$fid_score"
		echo ""
	} >>scores/"$cur_date".txt

done
