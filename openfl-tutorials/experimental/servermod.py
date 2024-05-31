from typing import List, Tuple

from flwr.server import ServerApp, ServerConfig
from flwr.server.strategy import FedAvg
from flwr.common import Metrics


# Define metric aggregation function
def weighted_average(metrics: List[Tuple[int, Metrics]]) -> Metrics:
    # Multiply accuracy of each client by number of examples used
    accuracies = [num_examples * m["accuracy"] for num_examples, m in metrics]
    examples = [num_examples for num_examples, _ in metrics]

    # Aggregate and return custom metric (weighted average)
    return {"accuracy": sum(accuracies) / sum(examples)}

#defining fitconfig
def fit_config(server_round: int):
    """Return training configuration dict for each round."""
    config = {
        "batch_size": 32,
        "current_round": server_round,
        "local_epochs": 2,
    }
    return config

#defining evaluateconfig
def evaluate_config(server_round: int):
    """Return training configuration dict for each round."""
    config = {
        "batch_size": 32,
        "current_round": server_round,
        "local_epochs": 2,
    }
    return config

# Define strategy
strategy = FedAvg(
    evaluate_metrics_aggregation_fn=weighted_average, 
    on_fit_config_fn=fit_config, # Received on client side within fit() fn=unction
    on_evaluate_config_fin=evaluate_config, #Received on Client side witin evaluate() function
    )

# Define config
config = ServerConfig(num_rounds=3)

# Flower ServerApp
app = ServerApp(
    config=config,
    strategy=strategy,
)


## Legacy mode
#if __name__ == "__main__":
#    from flwr.server import start_server
#
#    start_server(
#        server_address="0.0.0.0:8080",
#        config=config,
#        strategy=strategy,
#    )
#