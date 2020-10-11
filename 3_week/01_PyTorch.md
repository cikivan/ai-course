# PyTorch installation
You can use the tool `pip` to install any libraries by entering the following command to the Anaconda prompt:

For installing Pytorch you can generate your own command on [PyTorch](https://pytorch.org/). 
- <b> PyTorch Build </b> : Stable (1.4)
- <b> Your OS </b>: Depends on OS you have
- <b> Package </b>: Conda (AnacondaPrompt)
- <b> Language </b>: Python
- <b> CUDA </b>: If you have a Nvidia graphics card, select <i>10.1</i> (update the graphics card drive if you do not have the latest) or None if you have another graphics card

Now copy the Command and paste it to AnacacondaPrompt.

This installs PyTorch with all their dependencies. In case of errors please refer to the installation guides of [PyTorch](https://pytorch.org/).

## Checking your installation
Now we'll check whether all tools have been installed properly. In your virtual environment, start python by typing `python` and try to import PyTorch:

```
import torch
print(torch.__version__)
```

Additionally, to check if your GPU driver and CUDA is enabled and accessible by PyTorch, run the following commands to return whether or not the CUDA driver is enabled:

```
import torch
torch.cuda.is_available()
```

The first import might take a few seconds. If, during importing, an error occurs with one of the libraries, you need to upgrade it as in Step 1.3.

You can stop python running by typing `exit()` and then exiting Anaconda prompt.
