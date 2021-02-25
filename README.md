# Fast-Minimum-Norm-FMN-Attack

The Fast Minimum Norm Attack (FMN), from 
Fast Minimum-norm Adversarial Attacks through Adaptive Norm Constraints.

The attack is developed with [Foolbox](https://foolbox.readthedocs.io/en/stable/).

For a quick demo example, check out [this notebook](src/fmn_example.ipynb).

For a more complete example, with different datasets and robust models, check out 
the [full example notebook](src/fmn_demo.ipynb).

Here is a conceptual figure of the attack. In summary, the algorithm performs normalized 
gradient descent and projects into an epsilon Lp-ball which is adapted to 
find the minimum norm adversarials.

<img src="assets/gifs/path.gif" alt="path" width="400"/>

<small> GIF created with [SecML](https://secml.gitlab.io/).</small>

These are results against a MNIST 9-layer ConvNet. Check out the [notebooks](src/fmn_demo.ipynb) for more examples.

<img src="assets/images/examples_L0FMNAttack.png" alt="L0" style="width:200px;"/>
<img src="assets/images/examples_L1FMNAttack.png" alt="L1" style="width:200px;"/>
<img src="assets/images/examples_L2FMNAttack.png" alt="L2" style="width:200px;"/>
<img src="assets/images/examples_LInfFMNAttack.png" alt="LInf" style="width:200px;"/>
