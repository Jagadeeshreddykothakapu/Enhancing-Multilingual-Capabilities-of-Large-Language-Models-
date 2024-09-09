from fastchat.train.llama_flash_attn_monkey_patch import (
    replace_llama_attn_with_flash_attn,
)

replace_llama_attn_with_flash_attn()

from src.core.train import train  # noqa: E402

if __name__ == "__main__":
    train()
