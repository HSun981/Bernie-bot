import gpt_2_simple as gpt
import tensorflow
import os
import requests


model_name="124M"

if not os.path.isdir(os.path.join("models", model_name)):
    print(f"Downloading {model_name} model...")
    gpt2.download_gpt2(model_name=model_name)

sess = gpt2.start_tf_sess()

num_steps = 5

text_path = "sanderstweets.txt"

gpt2.finetune(sess,
              text_path,
              model_name=model_name,
              steps=num_steps
             )

gpt2.generate(sess)
single_text=gpt2.generate(sess, return_as_list=True)[0]
print(single_text)

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, checkpoint_dir="chkpt")
text = gpt2.generate(
    sess,
    checkpoint_dir="chkpt",
    length=10,
    temperature=1,
    destination_path="bernie.txt",
    prefix=None,
    return_as_list=True
)

generated_text = generate_text(checkpoint_dir, length, temperature, None, prefix)


