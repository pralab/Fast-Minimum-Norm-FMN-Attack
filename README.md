# Fast-Minimum-Norm-FMN-Attack

The Fast Minimum Norm Attack (FMN), from 
Fast Minimum-norm Adversarial Attacks through Adaptive Norm Constraints.

The attack is developed with [Foolbox](https://foolbox.readthedocs.io/en/stable/).

Here is a conceptual figure of the attack. The algorithm performes normalized 
gradient descent and projects into an epsilon Lp-ball which is adapted to 
find the minimum norm adversarials.

<img src="assets/gifs/path.gif" alt="path" width="50"/>

<small> GIF created with [SecML](https://secml.gitlab.io/).</small>

Finally, these are results against a MNIST 9-layer ConvNet.

<img src="assets/images/examples_L0FMNAttack.png" alt="L0" style="width:200px;"/>
<img src="assets/images/examples_L1FMNAttack.png" alt="L1" style="width:200px;"/>
<img src="assets/images/examples_L2FMNAttack.png" alt="L2" style="width:200px;"/>
<img src="assets/images/examples_LInfFMNAttack.png" alt="LInf" style="width:200px;"/>
