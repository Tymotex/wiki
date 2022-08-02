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
This section contains all the main things to know to be able to work on a Vue project.

### Writing Components
Components are defined in a single `.vue` file. Vue provides a template syntax that extends regular HTML.
```vue
<script>
export default {
    data() {
        return {
            message: "Hello world",
        };
    },
    methods: {
        handleClick() {
            this.message = "Goodbye world";
        },
    },
};
</script>

<template>
    <h1 v-on:click="handleClick">{{ message }}</h1>
</template>
```
You can embed any javascript expression inside the double braces, eg. `{{ 42 + Math.PI }}`

#### V- Directives
Directives start with `v-` and are introduced by Vue's template syntax. See the [full list of built-in directives](https://vuejs.org/api/built-in-directives.html).

- **Attribute/Prop binding** with `v-bind`, or the short-hand `:`.
	```vue
	<div v-bind:class="activeClass">Hi</div>
	<div :class="activeClass">Hi</div>       <!-- You can optionally omit v-bind and just use a colon
	                                              since attribute binding is so frequently used. -->
	```
- **[Conditional rendering](https://vuejs.org/guide/essentials/conditional.html)** with `v-if`, `v-else-if` and `v-else`. Whenever you use these, the elements must be consecutive siblings.
	```vue
	<script>
	export default {
	    data() {
	        return {
	            isDarkMode: false,
	        };
	    },
	    methods: {
	        toggleDarkMode() {
	            this.isDarkMode = !this.isDarkMode;
	        },
	    },
	};
	</script>
	<template>
	    <div v-if="isDarkMode" @click="toggleDarkMode">🌙</div>
	    <div v-else @click="toggleDarkMode">☀️</div>
	</template>
	```
- **[List rendering](https://vuejs.org/guide/essentials/list.html)** with `v-for`. 
- **Event listeners** with `v-on`, or the short-hand `@`.
	```vue
	<script>
	export default {
	    methods() {
	        handleClick: () => console.log('Hi');
	    }
	}
	</script>
	<template>
		<button v-on:click="handleClick">Hi</button>
	</template>
	```
	Combining `v-bind` and `v-on` lets you have *two-way data binding* where changes to the UI will change the state, and changing the state will change the UI. Alternatively you can use `v-model`.
- **Two-way data binding** with `v-model`. It's just syntactic sugar around `v-bind` and `v-on` for creating two-way [form bindings](https://vuejs.org/guide/essentials/forms.html).
	```vue
	<script>
	export default {
	    data() {
	        return {
	            email: "",
	        };
	    },
	};
	</script>
	
	<template>
	    <input v-model="email" />
	    <span>Value: {{ email }}</span>
	</template>
	```

