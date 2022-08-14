---
title: SVGs
description: SVGs
---

SVG (*scalable vector graphics*) is an image format that defines images using vectors in XML on a cartesian plane rather than pixels, like PNG or JPEG, which we call *bitmapped* or *raster* image formats.

Some advantages SVGs have over other image formats:
- Retains image quality at any zoom level, unlike .png files. This is the main advantage.
- For simple SVGs, it's easy to modify the image by tweaking the source code (which is just XML, usually).
- They are sometimes more performant if the image is not visually complex. For example, they're great for displaying icons on webpages.
- You can manipulate SVGs elements on a webpage with JavaScript and apply CSS styles to them, like regular HTML elements.

![[software-engineering/concepts/graphics/assets/raster-vs-vector.png|400]]

You can define any image using vectors or pixels, however which choice is better depends on how you expect to use the image. 
- For logos, SVGs are better.
- For diagrams, charts, figures, SVGs are better.
- For images with 'clean lines' and simple shapes, SVGs are probably better.
- For photographs, wallpapers and other images composed of very complex visuals, then SVGs aren't ideal because they'll be huge in size. 

## Drawing SVGs
It's hard to create SVGs by manually writing the XML code for the individual vectors that comprise an image. Instead, you should be using tools like Figma, Illustrator, Photoshop, etc. and you can also use some of these tools to convert between SVG and raster image formats. You can even use javascript libraries like [[software-engineering/technologies/D3|D3.js]] to create SVGs.

## SVG Elements
Just as HTML provides elements like `<p>`, `<div>`, `<table>` for describing documents, SVG provides elements like `<g>`, `<circle>`, `<line>` for defining images.

There are lot of SVG elements. See this [full reference on MDN](https://developer.mozilla.org/en-US/docs/Web/SVG/Element).

### Important Details
- In XML, you should specify the `xmlns` attribute which sets the XML namespace. Doing this is to [prevent name collisions](https://stackoverflow.com/questions/1181888/what-does-xmlns-in-xml-mean) where, for example, `<g>` might appear in a context outside of the SVG definition. Specifying the namespace removes the ambiguity about what `<g>` and other SVG elements are meant to do.
- Element ordering matters, just like in HTML. Elements defined later are rendered on top of previous elements.

### \<svg\>
`<svg>` is the root element of an image, just like how `<html>` is the root element of a document. You must always bind the `xmlns` to a namespace URI, eg. `<svg xmlns="http://www.23.org/2000/svg">`.

Using this element, we define the coordinate system:
![[software-engineering/concepts/graphics/assets/svg-coordinate-system.png|220]]
**Attributes**:
- `width` and `height` of the SVG container on an HTML document.
- `viewBox` defines the portion of the SVG 'canvas' to display.

### \<g\>
`<g>` groups together other basic shapes.

### \<circle\>, \<rect\>, \<line\>

### \<text\>

