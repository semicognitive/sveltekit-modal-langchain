<script lang="ts">
    import { enhance } from "$app/forms";

    let loading: boolean = false;
    let error: string | undefined;
    let summary: string | undefined;

    //Just an example of how to simply handle an endpoint - your endpoints act just like any other!
    function api_summarize() {
        loading = true;
        error = undefined;
        summary = undefined;

        return ({ result }: any) => {
            loading = false;
            error = result.error;

            summary = result.summary;
        };
    }
</script>

<main class="flex flex-col space-y-2">
    <h1 class="text-3xl font-bold underline">PDF Summarizer</h1>
    <p>Example made wiith <a target="_blank" rel="noopener noreferrer" class="underline" href="https://github.com/semicognitive/sveltekit-modal/tree/main">sveltekit-modal</a>.</p>

    <form method="POST" action="/api/summarize" use:enhance={api_summarize} on:change={() => ((error = undefined), (summary = undefined))} class="flex flex-col space-y-2 md:min-w-[28rem] lg:min-w-[32rem] xl:min-w-[36rem] max-w-6xl">
        <label class="flex flex-col items-center justify-center w-full h-64 border-2 border-neutral-300 border-dashed rounded-lg cursor-pointer bg-neutral-50">
            <div class="flex flex-col items-center justify-center py-6">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-10 h-10 mb-3 text-neutral-400">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5" />
                </svg>

                <p class="mb-2 text-sm text-neutral-500"><span class="font-semibold">Click to upload</span> or drag and drop</p>
                <p class="text-xs text-neutral-500">PDF</p>
            </div>
            <input type="file" name="document" accept="application/pdf" class="hidden" />
        </label>

        <span class="flex flex-row  space-x-4 ml-auto">
            {#if error}
                <span class="my-auto text-red-500">{error}</span>
            {/if}
            {#if loading}
                <svg class="my-auto animate-spin h-5 w-5 text-black" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                </svg>
            {/if}
            <button
                type="submit"
                class="inline-flex items-center rounded-md border border-transparent bg-neutral-800 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-black focus:outline-none focus:ring-2 focus:ring-black focus:ring-offset-2">
                Summarize!
            </button>
        </span>

        {#if summary}
            <div class="h-10" />
            <article class="prose">
                Summary: {@html summary}
            </article>
        {/if}
    </form>
</main>
