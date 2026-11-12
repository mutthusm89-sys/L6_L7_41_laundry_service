
def parse_order(text):
    if not isinstance(text, str):
        raise ValueError("Order must be a string")

    parts = text.split(":")
    if len(parts) != 2:
        raise ValueError("Use garment:weight format")

    garment, kg = parts
    garment = garment.strip().lower()

    if garment not in ["regular", "premium", "delicate"]:
        raise ValueError("Invalid garment type")

    try:
        kg = float(kg.strip())
    except ValueError:
        raise ValueError("Weight must be a number")

    if not 0 < kg < float("inf"):
        raise ValueError("Weight must be positive and finite")

    return garment.capitalize(), kg


def weight_average(weights_csv):
    if not isinstance(weights_csv, str):
        raise ValueError("Weights must be a string")

    if not weights_csv.strip():
        raise ValueError("Weight list cannot be empty")

    try:
        values = [float(x.strip()) for x in weights_csv.split(",")]
    except ValueError:
        raise ValueError("All weights must be numbers")

    if any(not (0 < x < float("inf")) for x in values):
        raise ValueError("Weights must be positive and finite")

    return sum(values) / len(values)


def payable_charge(text):
    if not isinstance(text, str):
        raise ValueError("Charge must be a string")

    parts = text.split("|")
    if len(parts) != 2:
        raise ValueError("Use charge|discount format")

    try:
        charge = float(parts[0].strip())
        discount = float(parts[1].strip())
    except ValueError:
        raise ValueError("Charge and discount must be numbers")

    if not (0 <= charge < float("inf")):
        raise ValueError("Charge must be non-negative and finite")

    if not (0 <= discount <= 100):
        raise ValueError("Discount must be between 0 and 100")

    discounted_charge = charge * (1 - discount / 100)
    return discounted_charge * 1.18


def main():
    print("==== Running parse_order ====")
    user_input = input("Enter garment:weight (e.g. regular:6): ")
    try:
        print("Garment and Weight:", parse_order(user_input))
    except ValueError as e:
        print("Error:", e)

    print("\n==== Running weight_average ====")
    user_input = input("Enter garment weights (e.g. 3,5,8): ")
    try:
        print("Average Weight:", round(weight_average(user_input), 2))
    except ValueError as e:
        print("Error:", e)

    print("\n==== Running payable_charge ====")
    user_input = input("Enter charge|discount (e.g. 300|40): ")
    try:
        print("Payable Charge:", round(payable_charge(user_input), 2))
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
