import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

import { sveltekit_modal } from 'sveltekit-modal/vite';

export default defineConfig({
	plugins: [sveltekit_modal(), sveltekit()]
});
