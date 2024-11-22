# Python program to suggest suitable clothing based on temperature

def suggest_clothing(temp):
    if temp > 20:
        return "It's warm enough to wear light and soft clothes."
    elif 10 <= temp <= 20:
        return "You might want to wear a light jacket."
    else:
        return "It's cold! Better stick with your jacket and pullover."

# Example usage
temperature = float(input("Enter the current temperature in Celsius: "))
suggestion = suggest_clothing(temperature)
print(suggestion)

