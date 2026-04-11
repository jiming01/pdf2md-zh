import re
text = "Unbiased KL Estimate Given  $ o_{i,t} $ is sampled from the old policy  $ \pi_{\text{old}}(\cdot|q,o_{i,\text{st}}) $, we correct the K3 estimator (Schulman, 2020) to obtain an unbiased KL estimate using the importance-sampling ratio between the current policy  $ \pi_{\theta} $ and the old policy  $ \pi_{\text{old}} $."
text = re.sub(r"(?<!\$)\$\s+([^$]+?)\s+\$(?!\$)", r"$\1$", text)
print(text)