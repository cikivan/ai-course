# (SK) Inštalácia TensorFlow a Keras
TensorFlow a Keras ako aj ďalšie knižnice nainštalujete pomocou `pip`. Do príkazového riadku Anacondy (uistite sa že vaše virtuálne prostredie je aktivované) zadajte príkazy:

```
pip install tensorflow
pip install keras
```

Knižnice `TensorFlow` a `Keras` sa nainštalujú automaticky spolu s potrebnými závislosťami. V prípade problémov sa obráťte na stránky [TensorFlow](https://www.tensorflow.org/install/pip) a [Keras](https://keras.io/#installation).

## Skontrolujte si inštaláciu
V príkazovom riadku Anacondy spusťte Python zadaním príkazu `python` (alebo názov podľa bodu 1.3) a následne skúsťte naimportovať nainštalované knižnice:

```
import tensorflow
import keras
```

Prvý import môže potrvať niekoľko sekúnd. Ak počas importu sa vyskytnú problémy s niektorou knižnicou, potrebujete si ju aktualizovať podľa príkazov uvedených v bode 1.4.

Python zastavíte zadaním príkazu `exit()`.

## (EN) Installing TensorFlow and Keras
You can use the tool `pip` to install any libraries by entering the following command to the Anaconda prompt:

```
python -m pip install tensorflow
python -m pip install keras
```

This installs `TensorFlow` and `Keras` with all their dependencies. In case of errors please refer to the installation guides of [TensorFlow](https://www.tensorflow.org/install/pip) or [Keras](https://keras.io/#installation).

##  Checking your installation
Now we'll check whether all tools have been installed properly. In your virtual environment, start python by typing `python` and try to import TensorFlow and Keras:

```
import tensorflow
import keras
```

The first import might take a few seconds. If, during importing, an error occurs with one of the libraries, you need to upgrade it as in Step 1.3.

You can stop python running by typing `exit()` and then exiting Anaconda prompt.