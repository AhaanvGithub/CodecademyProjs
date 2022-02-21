weight = 5

# Ground shipping premium
premium_price = 125

# Ground price & drone price
ground_price = 0
drone_price = 0

# Ground price
if weight < 2:
  ground_price = 20 + (weight * 1.5)
  drone_price = 4.5 * weight
elif weight > 2 and weight <= 6:
  ground_price = 20 + (weight * 3)
  drone_price = weight * 9
elif weight > 6 and weight <= 10:
  ground_price = 20 + (weight * 4)
  drone_price = weight * 12
elif weight > 10:
  ground_price = 20 + (weight * 4.75)
  drone_price = weight * 14.25

print("Depending on the weight of your package,")
print("Ground Shipping: " + str(ground_price))
print("Ground Premium Shipping: 125")
print("Drone Shipping: " + str(drone_price))

cheapest = ""

if ground_price < drone_price and ground_price < 125:
  cheapest = "Ground Shipping for " + str(ground_price)
elif drone_price < ground_price and drone_price < 125:
  cheapest = "Drone Shipping for " + str(drone_price)
elif drone_price > 125 and ground_price > 125:
  cheapest = "Premium Ground Shipping for 125"

print("\nThe cheapest is about, " + cheapest)
