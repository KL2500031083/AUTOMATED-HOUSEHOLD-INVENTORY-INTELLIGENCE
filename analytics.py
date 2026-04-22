import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def show_analysis(items):
    if not items:
        print("No data")
        return

    df = pd.DataFrame([
        {"name": i.name, "quantity": i.quantity}
        for i in items.values()
    ])

    print("\nTotal Items:", np.sum(df["quantity"]))

    df.plot(x="name", y="quantity", kind="bar")
    plt.title("Inventory Quantity")
    plt.show()