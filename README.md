# Fast-Minimum-Norm (FMN) Attack

The Fast Minimum Norm Attack (FMN), from 
Fast Minimum-norm Adversarial Attacks through Adaptive Norm Constraints.

:dart: Accepted at NeurIPS 2021! 
Paper available at [this link](https://proceedings.neurips.cc/paper/2021/hash/a709909b1ea5c2bee24248203b1728a5-Abstract.html).

🎉 Now available also in [Foolbox](https://github.com/bethgelab/foolbox), [SecML](https://github.com/pralab/secml) and  [Adversarial Library](https://github.com/jeromerony/adversarial-library).

:video_game: For a quick demo example, check out [this notebook](src/fmn_example.ipynb).

:pencil: For a more complete example, with different datasets and robust models, check out 
the [full example notebook](src/fmn_demo.ipynb).

Here is a conceptual figure of the attack. In summary, the algorithm performs normalized 
gradient descent and projects into an epsilon Lp-ball which is adapted to 
find the minimum norm adversarials.

<p align="center">
<img src="assets/gifs/path.gif" alt="path" width="400"/>
  </p>

<small> GIF created with [SecML](https://secml.gitlab.io/) library.</small>

## Using FMN from this repository

```python
from src.attacks.fmn import L1FMNAttack
import foolbox as fb

model = ...  # pytorch model
fb_model = fb.models.PyTorchModel(model)
attack = L1FMNAttack()
advs, _, is_adv = attack(fb_model, images, criterion, epsilons=None)

```

## Using FMN from Foolbox

```python
import foolbox as fb

model = ...  # pytorch model
fb_model = fb.models.PyTorchModel(model)
attack = fb.attacks.L1FMNAttack()
advs, _, is_adv = attack(fb_model, samples, labels, epsilons=None)

```

## Using FMN from SecML (using the Foolbox Wrapper)

```python
import foolbox as fb
from secml.adv.attacks.evasion import CAttackEvasionFoolbox

model = ...  # pytorch model
secml_model = CClassifierPyTorch(model=model, pretrained=True, ...)  # wraps pytorch model in Secml
attack = CAttackEvasionFoolbox(secml_model, y_target=None, fb_attack_class=fb.attacks.L1FMNAttack)
y_pred, _, adv_ds, _ = attack.run(samples, labels)

```

## Using FMN from Adversarial Library


```python
from adv_lib.attacks import fmn

model = ...  # pytorch model
norm = 1  # will use L1 norm
results = fmn(model, inputs, labels, norm)

```

# Preview of the results

These are results against a MNIST 9-layer ConvNet. Check out the [notebooks](src/fmn_demo.ipynb) for more examples.

<p align="center">
<img src="assets/images/examples_L0FMNAttack.png" alt="L0" style="width:700px;"/>
<img src="assets/images/examples_L1FMNAttack.png" alt="L1" style="width:700px;"/>
<img src="assets/images/examples_L2FMNAttack.png" alt="L2" style="width:700px;"/>
<img src="assets/images/examples_LInfFMNAttack.png" alt="LInf" style="width:700px;"/>
<p>
  
# :book:  Cite this work

If you use FMN in your work, please cite us using the following BibTeX entry:

```
@article{pintor2021fast,
  title={Fast minimum-norm adversarial attacks through adaptive norm constraints},
  author={Pintor, Maura and Roli, Fabio and Brendel, Wieland and Biggio, Battista},
  journal={Advances in Neural Information Processing Systems},
  volume={34},
  year={2021}
}
```
