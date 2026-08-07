import os
import time
import matplotlib.pyplot as plt

gravities = {
    "Mercury": 3.70,
    "Venus": 8.87,
    "Earth": 9.81,
    "Moon": 1.62,
    "Mars": 3.71,
    "Jupiter": 24.79,
    "Saturn": 10.44,
    "Uranus": 8.69,
    "Neptune": 11.15,
    "Pluto": 0.62
}

planets = [
   "Earth",
   "Mercury",
   "Venus",
   "Moon",
   "Mars",
   "Jupiter",
   "Saturn",
   "Uranus",
   "Neptune",
   "Pluto"
]


introduction = 'Hello ! This is a Solar System Kinematics Simulator. I am a 9th-grade physics enthusiast, at the time of this project, I have been studying physics for one month. I hope you enjoy this simulator and learn something new about planetary motion. More information is available in the "Readme" file regarding the calculations and the logic behind the simulator.'


for into in introduction:
   print(into, end='', flush=True)
   time.sleep(0.05)

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')



while True:

    selected_planets = []

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Available Planets:")
        for planet in planets:
            if planet not in selected_planets:
                print(f" - {planet}")

        print(f"\nSelected planets: {selected_planets}")

        option = input('Choose a planet: (or type "compare" to finish the selection.):').strip().capitalize()

        if option == "Compare":
            if len(selected_planets) < 2:
                print("Please select at least two planets to compare.")
                continue
            else:
                break

        if option in planets and option not in selected_planets:
            selected_planets.append(option)
        else:
            print("Not found in database.")


    h_earth = float(input("Enter your jump height on earth (in meters): "))

    g_earth = gravities["Earth"]
    v0 = (2 * g_earth * h_earth) ** 0.5
    
    text = "Running simulation and comparing the results"
    points = "..."

    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)

    for point in points:
        print(point, end='', flush=True)
        time.sleep(0.7)

    plt.figure(num="Computational Kinematics Analysis - Nicolas S. Araujo", figsize=(10, 6))

    for planet in selected_planets:
        g_current = gravities[planet]
        t_total = (v0 / g_current) * 2
        h_max = (v0 ** 2) / (2 * g_current)

        times = []
        heights = []
        t_current = 0
        walk = 0.01

        while t_current <= t_total:
            times.append(t_current)
            h = (v0 * t_current) - (g_current * (t_current ** 2)) / 2
            heights.append(h)
            t_current += walk

        plt.plot(times, heights, label=f"{planet} (H: {h_max:.2f}m | T: {t_total:.2f}s)")

    plt.title(f"Planetary Jump Comparison: Computational Kinematics Analysis", fontsize=12, pad=15)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Height (meters)")
    plt.legend()
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    
    print("\n Opening the graphical simulator window!")
    plt.tight_layout()
    plt.show()

    leave = input("\nDo you want to leave the simulator? (yes/no): ").strip().lower()

    if leave == 'yes':
        print("\nThank you for using the planetary gravity simulator !")
        break

# If anyone is reading this, I am a Brazilian student, If you find any mistakes on code or in the english, let me know, I would be very grateful. My dream is to study at MIT one day. I hope I can make it there!
# My Discord: morthril.