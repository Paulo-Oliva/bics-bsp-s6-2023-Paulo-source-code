function downloadImage()
{
	const div = document.getElementById("result");
	const img = div.getElementsByTagName("img")[0];
	let link = document.createElement("a");

	link.href = img.src;
	link.download = "result.png";
	link.click();
}

function addEvent()
{
	let downloadButton = document.getElementById("download");
	downloadButton.addEventListener("click", downloadImage);
}


document.addEventListener('DOMContentLoaded', addEvent);