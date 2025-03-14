from huggingface_hub import snapshot_download

snapshot_download(
    repo_type = "model",
    repo_id = "Qwen/Qwen2.5-1.5B-Instruct",
    local_dir = "/aiarena/group/gmgroup/fanhy/model/Qwen2.5-1.5B-Instruct",
    resume_download = True,
    local_dir_use_symlinks = False
)
