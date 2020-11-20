import math

def kl_divergence(p,q):
    divergence = 0
    for num in range(len(p)):
        if p[num] != 0 and q[num] != 0:
            divergence -= p[num] * math.log(p[num]/q[num])
        else:
            divergence -= 0
    return divergence



true_distribution = [0.05, 0.2, 0.5, 0.2, 0.05]

justin_s = kl_divergence([0.05, 0.2, 0.5, 0.2, 0.05], true_distribution)


nathan_r = kl_divergence([0.05, 0.2, 0.35, 0.35, 0.05],true_distribution)


justin_h = kl_divergence([0.1, 0.2, 0.35, 0.25, 0.1], true_distribution)


nathan_a = kl_divergence([0.1, 0.25, 0.4, 0.1, 0.15], true_distribution) 


cayden = kl_divergence([0.05, 0.3, 0.35, 0.2, 0.1], true_distribution)


maia = kl_divergence([0.1, 0.1, 0.4, 0.25, 0.15], true_distribution)


spencer = kl_divergence([0.05, 0.35, 0.4, 0.15, 0.05], true_distribution)


charlie = kl_divergence([0.05, 0.25, 0.45, 0.2, 0.05], true_distribution)


anton = kl_divergence([0.1, 0.25, 0.35, 0.2, 0.1], true_distribution)


william = kl_divergence([0.05, 0.25, 0.4, 0.3, 0], true_distribution)


best_to_worst = ["Charlie: {}".format(charlie), "Spencer: {}".format(spencer), "Cayden: {}".format(cayden), "Anton: {}".format(anton), "Justin H: {}".format(justin_h), "Nathan R: {}".format(nathan_r), "William: {}".format(william), "Nathan A: {}".format(nathan_a), "Maia: {}".format(maia)]
print(best_to_worst)
print("The person who best simulated a completely random approximation was Charlie, excluding Justin S, who got the true distribution.")


