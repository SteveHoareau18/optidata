# app/config.py

SECRET_KEY = "2970c929a998c1efbcd2a7d06f7f748267c5f2f9dda33b3283739131a7a3feea410ed1831e4addade8200c5008db4619fdd965258d1d7e3f0241a8f9a0898001f162c294fb2dddf3d31b33188fb0f5b7f388a03789feaa6bcedaf3352cb805c129edcdafbf481ba74e48ba82b2fcc1f26f62473ac91a5de59a2e1639e92b19368caa4f0d77f68b1050168a0b7f1c5de5b6e7c818ee51263bfed40283f22d80b45742c32b4ec75c86d29b6b68dbbd085251f332b83dc9e2230e9b607d312da4da82aea1a48e7659099bddebc63a444996c28d83318b7347722c7d593067da44f3ff74480fad5c86f6ffb1edbe479099daa0068348386bcc0af20343454f29da6b"  # À changer
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Par exemple 30 minutes
DATABASE_URL = "postgresql://admin:secret@localhost:5432/optidata"
