# torch imports
import torch
import torch.nn as nn
from torchvision.models import ViT_B_16_Weights, vit_b_16

# custom imports
from niche import Niche_Model


class Niche_ViT(Niche_Model):
    def __init__(self):
        super(Niche_ViT, self).__init__()
        weights = ViT_B_16_Weights.IMAGENET1K_SWAG_E2E_V1
        self.model = vit_b_16(weights=weights)
        self.model.heads = nn.Linear(self.model.heads.in_features, 2)

    def forward(self, x):
        return self.model(x)
