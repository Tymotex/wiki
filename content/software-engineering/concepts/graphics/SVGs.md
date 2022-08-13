---
title: SVGs
description: SVGs
---

SVG (*scalable vector graphics*) is an image format that defines images using vectors rather than pixels, like PNG or JPEG, which we call *bitmap* or *raster* image formats. 

Some advantages SVGs have over other image formats:
- Retains image quality at any zoom level, unlike .png files. This is the main advantage.
- For simple SVGs, it's easy to modify the image by tweaking the source code (which is just XML, usually).
- They are more performant if the image is not visually complex. For example, they're great for displaying icons on webpages.
- You can manipulate SVGs elements on a webpage with JavaScript and apply CSS styles to them, like regular HTML elements.

You can define any image using vectors or pixels, however which choice is better depends on how you expect to use the image. 
- For logos, SVGs are better.
- For diagrams and charts, SVGs are better.
- For images with 'clean lines' and simple shapes, SVGs are probably better.
- For photographs, wallpapers and other images composed of very complex visuals, then SVGs aren't ideal because they'll be huge in size. 

You can use Photoshop, Illustrator or Gimp to convert images to SVGs and vice versa.

## Creating SVGs
It's hard to create SVGs by manually writing the XML code for the individual vectors that comprise an image. Instead, you should be using tools like Figma, Illustrator, Photoshop, etc. You can even use javascript libraries like [[software-engineering/technologies/D3|D3.js]].
