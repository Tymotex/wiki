---
title: Vue.js
description: Vue.js
---

![[software-engineering/technologies/assets/vue-wallpaper.png|600]]

Vue.js is a [[software-engineering/programming-languages/JavaScript|JavaScript]] framework for building sophisticated UI components in a reusable, maintainable and performant way. Just like for React, there's a rich ecosystem of npm packages you can plug in to have things like: unit testing, static site generation, client-side routing, state management, etc.

## Setup
Just run the following.
```bash
npm init vue@latest  # Invokes `create-vue` which presents a terminal menu
                     # with prompts to help set up your project.
```

## Core Things to Know
This section contains all the main things you need to know to work on a Vue project.

### Writing Components
Components are defined in a single `.vue` file. Vue provides a template syntax that extends regular HTML.

```html
<script>
export default {
	data() {
		return {
			message: "Hello world"
		}
	}
}
</script>

<template>
	<h1>{{ message }}</h1>
</template>
```
You can embed any javascript expression inside the double braces `{{ 42 + 24 }}`

