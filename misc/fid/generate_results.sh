#!/bin/bash

TRAINING_DIR=$1
MODELS_DIR=$2
shift 2
ARGS=("$@")

# Get the current directory
SCRIPT_DIR=$(pwd)

# If any argument is missing, print an error message and exit
if [ -z "$TRAINING_DIR" ] || [ -z "$MODELS_DIR" ]; then
	echo "Usage: $0 <training_dir> <models_dir>"
	exit 1
fi

# Check if the source directory exists
if [ ! -d "$MODELS_DIR" ]; then
	echo "Models directory does not exist: $MODELS_DIR"
	exit 1
fi
# Check if the script directory exists
if [ ! -d "$TRAINING_DIR" ]; then
	echo "Training directory does not exist: $TRAINING_DIR"
	exit 1
fi

# Save the name of the dir containing the models
MODEL_NAME=$(basename "$MODELS_DIR")

# Iterate over each file in the models directory
for file in "$MODELS_DIR"/*; do
	if [ -f "$file" ]; then
		# Get the epoch number from the file name
		epoch=$(basename "$file" | cut -d'_' -f1)

		# Copy the file to the predefined location inside the training directory
		cp "$file" "$TRAINING_DIR/checkpoints/pixelart/latest_net_G.pth"

		# Change to the script directory
		cd "$TRAINING_DIR" || exit

		# Run the python script with the specified arguments
		python test.py --dataroot datasets/pixelart/testA --model test --name pixelart --no_dropout --num_test 454 "${ARGS[@]}"

		# Check if the python script ran successfully
		if [ $? -ne 0 ]; then
			echo "Python script failed for file: $file"
			exit 1
		fi

		# Create the images directory if it doesn't exist
		mkdir -p "$SCRIPT_DIR/images/$MODEL_NAME/$epoch"

		# Copy all files ending with "_fake.png" to the images directory inside the script directory
		cd "$SCRIPT_DIR" || exit
		cp "$TRAINING_DIR/results/pixelart/test_latest/images/"*"_fake.png" "$SCRIPT_DIR/images/$MODEL_NAME/$epoch"
	fi
done

echo "Done generating results for all models in the $MODELS_DIR directory."
