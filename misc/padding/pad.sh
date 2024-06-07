#!/bin/bash

# for each file in the input directory
for file in $1; do
	filename=$(basename "$file")
	magick "$file" -gravity center -background none -extent "%[fx:max(w,h)]x%[fx:max(w,h)]" out/"$filename"
done

