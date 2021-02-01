from collections import namedtuple

Model = namedtuple('Model', 'model_name model_url '
                            'module_name task transform model_kwargs')

models = [
    Model('MnistClean', 'https://github.com/maurapintor/mnist-pretrained',
          'foolbox_model', 'MNIST',
          lambda x: x, {}),
    Model('MnistChallenge', 'https://github.com/maurapintor/mnist-pretrained',
          'foolbox_madry_mnist', 'MNIST',
          lambda x: x, {}),
    Model('Rony2019DDNMnist', 'https://github.com/maurapintor/fast_adversarial',
          'foolbox_model', 'MNIST', lambda x: x, {'dataset': 'MNIST'}),
    Model('Carmon2019Unlabeled', 'https://github.com/maurapintor/robustbench-foolbox',
          'foolbox_robustbench', 'CIFAR10',
          lambda x: x, {'model_name': 'Carmon2019Unlabeled', 'norm': 'Linf'}),
    Model('Rony2019DDNCifar10', 'https://github.com/maurapintor/robustbench-foolbox',
          'foolbox_robustbench', 'CIFAR10',
          lambda x: x, {'model_name': 'Rony2019Decoupling', 'norm': 'L2'}),
    Model('Cifar10Challenge', 'https://github.com/maurapintor/robustbench-foolbox',
          'foolbox_robustbench', 'CIFAR10',
          lambda x: x, {'model_name': 'Engstrom2019Robustness', 'norm': 'Linf'}),
]
