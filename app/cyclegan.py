import subprocess
import shutil
import os


def convert_image(folder, options, model):
    # Path to the directory where the script is located
    script_dir = "../training"
    # Copy the selected model inside static/models to the training folder and rename it to latest_net_G.pth
    shutil.copy(f"static/models/{model}", f"{script_dir}/checkpoints/pixelart/latest_net_G.pth")
    # Command to execute
    command = [
        "python", "test.py", "--model", "test", "--dataroot", folder, "--name", "pixelart", "--no_dropout",
        "--num_test", "1"
    ]

    for key, value in options.items():
        if value:
            command.extend([f"--{key}", value])

    converted_image_path = os.path.join("..", "training", "results", "pixelart", "test_latest", "images")
    # Delete all the files in the folder
    for file in os.listdir(converted_image_path):
        os.remove(os.path.join(converted_image_path, file))

    process = subprocess.Popen(command, cwd=script_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    _, error = process.communicate()

    if error:
        raise Exception(error)

    for file in os.listdir(converted_image_path):
        if "fake" in file:
            converted_image_path = os.path.join(converted_image_path, file)
            break

    # Copy the converted image to the static folder
    destination = shutil.copy(converted_image_path, "static/uploads/")

    return os.path.basename(destination)
