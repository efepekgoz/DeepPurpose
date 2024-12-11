import matplotlib.pyplot as plt

# Data for the chart with 'CNS' and 'Arthritis and Pain' switched
categories = ['CNS', 'Cardiovascular', 'Arthritis and Pain', 'Infectious Disease', 'Oncology', 
              'Ophthalmology', 'Metabolic Disease', 'Urology', "Women's Health", 'All']
values = [8, 19, 17, 17, 5, 15, 13, 10, 6, 11]

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Adjust the width and spacing of the bars
bars = ax.bar(categories, values, color='skyblue', edgecolor='black', width=0.8)

# Highlight the 'All' bar
bars[-1].set_color('gray')

# Labels
ax.set_ylabel('Percentage of success')
ax.set_ylim(0, 20)

# Set specific y-axis ticks
ax.set_yticks([0, 5, 10, 15, 20])

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Annotating the 'All' bar
ax.text(len(values) - 1, values[-1] + 0.5, '11%', ha='center', va='bottom', color='black', fontsize=10)

# Reduce spacing between bars
plt.margins(x=0.01)  # Adjust the margin to make columns closer

# Set the background to transparent
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)

# Remove the title
plt.tight_layout()
plt.show()
