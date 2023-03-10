import modal

config = {
    'name': 'sveltekit-example',
    'log': False,
    'stub_asgi': {
        'image': modal.Image.debian_slim().pip_install("python-multipart", "gpt-index", "langchain", "openai", "pylibmagic", "pypdf"),
        'secret': modal.Secret.from_name("my-openai-secret")
    }
}