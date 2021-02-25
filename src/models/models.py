from collections import namedtuple

Model = namedtuple('Model', 'model_name model_url '
                            'module_name task transform model_kwargs')

models = [
    Model('MnistClean', 'https://github.com/maurapintor/mnist-pretrained',  #0
          'foolbox_model', 'MNIST',
          lambda x: x, {}),
    Model('MnistChallenge', 'https://github.com/maurapintor/mnist-pretrained',  #1
          'foolbox_madry_mnist', 'MNIST',
          lambda x: x, {}),
    Model('Rony2019DDNMnist', 'https://github.com/maurapintor/fast_adversarial',  #2
          'foolbox_model', 'MNIST', lambda x: x, {'dataset': 'MNIST'}),
    Model('Carmon2019Unlabeled', 'https://github.com/maurapintor/robustbench-foolbox',  #3
          'foolbox_robustbench', 'CIFAR10',
          lambda x: x, {'model_name': 'Carmon2019Unlabeled', 'norm': 'Linf'}),
    Model('Rony2019DDNCifar10', 'https://github.com/maurapintor/robustbench-foolbox',  #4
          'foolbox_robustbench', 'CIFAR10',
          lambda x: x, {'model_name': 'Rony2019Decoupling', 'norm': 'L2'}),
    Model('Cifar10Challenge', 'https://github.com/maurapintor/robustness',  #5
          'fb.load_cifar_models', 'CIFAR10',
          lambda x: x, {'model_id': 'l-inf-8/255'}),
]
