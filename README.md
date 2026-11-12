# Red Panda Leaf Hug — Make the cutest picture (variant)

## Concept
A baby red panda cub with huge glossy dark eyes, fluffy rust-red fur and cream cheeks, head tilted, hugging a small green bamboo leaf with both paws. Soft pastel mint background with bokeh.

Original AI-generated artwork made for this entry (make.fun bounty
"Make the cutest picture", $250, ends Fri 13 Nov 2026 17:00 WIB). Not stock,
not anyone else's work, and a different subject/concept from the main entry
(baby sea otter hugging a pink heart) and from the other variants.

## How it was made
Generated with an image-generation pipeline from a text prompt, then resized
1600x1600 -> 896x896 with PIL Lanczos and saved as PNG. No text or watermark
in the image.

## Jury rubric mapping (RULES.txt)
1. **Cute at a glance** — one subject fills almost the whole frame.
2. **Cute subject** — round soft shape, huge sparkling eyes, small/chubby
   proportions, smiling expression.
3. **Charm** — one personality touch: hugging the bamboo leaf with both paws.
4. **Craft** — clean render, correct eyes/ears/limbs, no artefacts, no text.
5. **Readable small** — the large single subject stays clear at ~300 px.

## Verification
- `entry.png`: PNG 896x896, 924783 bytes (<= 1,048,576), magic bytes
  `89 50 4E 47`, SHA-256 `21a00d461ddfa1878564bc0a12056e6e1cb3c8e8d0367bb8ccbec6925acbf63b`.
- `main.py` (stdlib only) run 2x writes byte-identical output equal to
  `entry.png` (verified locally).

## Files
- `entry.png` — the entry image
- `main.py` — entrypoint: copies `entry.png` byte-for-byte to
  `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`)
- `LICENSE` — MIT
- `.makefun/owner.json` — wallet ownership proof
