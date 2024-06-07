#!/bin/bash

# Default values
SIZE=128x128
INPUT_DIR=.
OUTPUT_DIR=resized

usage() {
	echo "Usage: $0 [-s size] [-i input_dir] [-o output_dir]"
	echo "  -s size       Resize images to the specified size (default: 128x128)"
	echo "  -i input_dir  Directory containing the images to resize (default: current directory)"
	echo "  -o output_dir Directory to save the resized images (default: resized)"
	exit 1
}

# Parse command-line options
while getopts ":s:i:o:" opt; do
	case ${opt} in
	s)
		SIZE=$OPTARG
		;;
	i)
		INPUT_DIR=$OPTARG
		;;
	o)
		OUTPUT_DIR=$OPTARG
		;;
	\?)
		usage
		;;
	esac
done

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Loop through all image files in the current directory
for img in "$INPUT_DIR"/*.{jpg,jpeg,png}; do
	if [ -e "$img" ]; then
		magick "$img" -filter point -resize "$SIZE" "$OUTPUT_DIR/$(basename "$img")"
	fi
done

echo "All images have been resized and saved in the $OUTPUT_DIR directory."