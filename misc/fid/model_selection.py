import os
import shutil
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Model Selection")
    parser.add_argument("source_dir", type=str, help="Path to the source directory")
    parser.add_argument("target_dir", type=str, help="Path to the target directory")
    parser.add_argument("epochs", type=int, nargs="+", help="Epoch numbers")
    return parser.parse_args()


def select_models(source_dir, target_dir, epochs):
    # Get a list of all files in the source directory
    files = os.listdir(source_dir)
    # Create the target directory if it does not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    # Iterate over the files
    for file in files:
        # Check if the file name contains any of the specified epochs
        for epoch in epochs:
            if file.startswith(f"{epoch}_net_G_A"):
                # Construct the source and target paths
                source_path = os.path.join(source_dir, file)
                target_path = os.path.join(target_dir, file)
                # Copy the file to the target directory
                shutil.copy2(source_path, target_path)
    print(f"Models from epochs {epochs} have been copied to {target_dir}.")


if __name__ == "__main__":
    args = parse_args()
    select_models(args.source_dir, args.target_dir, args.epochs)
