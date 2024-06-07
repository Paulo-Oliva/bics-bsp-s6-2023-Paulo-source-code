// Function to preview the selected image
function previewImage(file)
{
	const dragDrop = document.querySelector(".drag-drop");
	let image = document.createElement("img");
	image.src = URL.createObjectURL(file);
	image.style.maxWidth = "40vw";
	image.style.maxHeight = "50vh";

	dragDrop.replaceChildren(image);
}

// Event handler for file input change
function handleFileInputChange(event)
{
	let file = event.target.files[0];
	if (file)
	{
		previewImage(file);
	}
}

// Event handler for drag over
function handleDragOver(event)
{
	event.preventDefault();
	event.dataTransfer.dropEffect = "copy";
}

// Event handler for drop
function handleDrop(event)
{
	event.preventDefault();
	let files = event.dataTransfer.files;
	if (files.length)
	{
		document.querySelector("input[type=file]").files = files;
		previewImage(files[0]);
	}
}

// Event handler for form submission
function handleSubmit(_)
{
	document.querySelector("form").submit();
}

// Prevent default drag over behavior outside the drag-drop area
function handleGlobalDragOver(event)
{
	if (!event.target.closest(".drag-drop"))
	{
		event.preventDefault();
		event.dataTransfer.dropEffect = "none";
	}
}

// Prevent default drop behavior outside the drag-drop area
function handleGlobalDrop(event)
{
	if (!event.target.closest(".drag-drop"))
	{
		event.preventDefault();
	}
}


function clearOptions(optionsContainer)
{
	while (optionsContainer.children.length > 3)
	{
		optionsContainer.removeChild(optionsContainer.lastChild);
	}
}


function addOption(optionsContainer, label, type, name, value)
{
	let option = document.createElement("div");
	option.classList.add("option");

	let labelElement = document.createElement("label");
	labelElement.setAttribute("for", name);
	labelElement.textContent = label;

	let inputElement = document.createElement("input");
	inputElement.setAttribute("type", type);
	inputElement.setAttribute("id", name);
	inputElement.setAttribute("name", name);
	inputElement.setAttribute("value", value);

	option.appendChild(labelElement);
	option.appendChild(inputElement);
	optionsContainer.appendChild(option);
}

// Function to handle the change event of the preprocessing select element
function handleOptionsChange()
{
	let optionsContainer = document.getElementById("options");
	const selectedOption = document.getElementById("preprocessing").value;

	clearOptions(optionsContainer);
	switch (selectedOption)
	{
		case "resize_and_crop":
			addOption(optionsContainer, "Load Size", "number", "load_size", "286");
			addOption(optionsContainer, "Crop Size", "number", "crop_size", "256");
			break;
		case "crop":
			addOption(optionsContainer, "Crop Size", "number", "crop_size", "256");
			break;
		case "scale_width":
			addOption(optionsContainer, "Width", "number", "crop_size", "256");
			break;
		case "scale_width_and_crop":
			addOption(optionsContainer, "Width", "number", "load_size", "286");
			addOption(optionsContainer, "Crop Size", "number", "crop_size", "256");
			break;
		default:
			break;
	}
}


// Set up event listeners
function initialize()
{
	let input = document.querySelector("input[type=file]");
	input.addEventListener("change", handleFileInputChange);

	let dragDrop = document.querySelector(".drag-drop");
	dragDrop.addEventListener("dragover", handleDragOver);
	dragDrop.addEventListener("drop", handleDrop);

	let submitButton = document.querySelector("input[type=submit]");
	submitButton.addEventListener("click", handleSubmit);

	let preprocessingSelect = document.getElementById("preprocessing");
	preprocessingSelect.addEventListener("change", handleOptionsChange);
	handleOptionsChange();

	document.addEventListener("dragover", handleGlobalDragOver);
	document.addEventListener("drop", handleGlobalDrop);
}

// Initialize the event listeners
document.addEventListener("DOMContentLoaded", initialize);