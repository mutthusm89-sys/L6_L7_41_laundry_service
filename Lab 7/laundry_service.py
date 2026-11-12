
def parse_order(text):
    if not isinstance(text, str):
        raise ValueError("Order must be a string")

    if ":" not in text:
        raise ValueError("Invalid order format. Use garment:weight")

    parts = text.split(":")

    if len(parts) != 2:
        raise ValueError("Invalid order format")

    garment, kg = parts

    garment = garment.strip().lower()

    if garment not in ["regular", "premium", "delicate"]:
        raise ValueError("Invalid garment type")

    try:
        kg = float(kg.strip())
    except (ValueError, AttributeError):
        raise ValueError("Weight must be a number")

    if kg <= 0:
        raise ValueError("Weight must be positive")

    return garment.capitalize(), kg


def weight_average(text):
    if not isinstance(text, str):
        raise ValueError("Weights must be a string")

    if not text.strip():
        raise ValueError("Weight list cannot be empty")

    try:
        weights = [float(x.strip()) for x in text.split(",")]
    except ValueError:
        raise ValueError("All weights must be numbers")

    if any(w <= 0 for w in weights):
        raise ValueError("Weights must be positive")

    return sum(weights) / len(weights)


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

    if charge < 0:
        raise ValueError("Charge cannot be negative")

    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100")

    discounted_charge = charge - (charge * discount / 100)

    return discounted_charge * 1.18


def main():
    print("==== Running parse_order ====")
    user_input = input(
        "Enter garment:weight in kg (e.g. regular:6): "
    )
    try:
        result = parse_order(user_input)
        print("Garment and Weight:", result)
    except ValueError as e:
        print("Error:", e)

    print("\n==== Running weight_average ====")
    user_input = input(
        "Enter garment weights as CSV (e.g. 3,5,8): "
    )
    try:
        result = weight_average(user_input)
        print("Average Weight:", round(result, 2))
    except ValueError as e:
        print("Error:", e)

    print("\n==== Running payable_charge ====")
    user_input = input(
        "Enter charge|discount (e.g. 300|40): "
    )
    try:
        result = payable_charge(user_input)
        print("Payable Charge:", round(result, 2))
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
