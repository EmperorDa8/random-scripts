def car_listing(car_prices):
  if car_prices=="":
    return ""
  else:
    result = ""
    for brand, cost in car_prices.items():
      result += f"{brand} costs {cost} dollars"+"\n"
    return result

#print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))
