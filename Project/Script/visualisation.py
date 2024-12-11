import re
import matplotlib.pyplot as plt

training_losses = []

with open('/Users/efepekgoz/Project/csv_files/your_log_file2.txt', 'r') as file:
    for line in file:
        # Use regex to find lines containing "Training at Epoch" and "loss"
        match = re.search(r'Training at Epoch \d+ iteration \d+ with loss ([\d\.]+)', line)
        if match:
            loss_value = match.group(1).rstrip('.')  
            training_losses.append(float(loss_value))

#print(training_losses)

validation_losses = []

with open('/Users/efepekgoz/Project/csv_files/your_log_file2.txt', 'r') as file:
    for line in file:
        # Use regex to find lines containing "Validation at Epoch" and "loss"
        match = re.search(r'Validation at Epoch \d+ with loss:([\d\.]+)', line)
        if match:
            loss_value = match.group(1).rstrip('.') 
            validation_losses.append(float(loss_value))

print(validation_losses)

epochs = range(1, len(validation_losses) + 1)

plt.figure(figsize=(10, 6))
plt.plot(epochs, training_losses[:len(validation_losses)], label='Training Loss')
plt.plot(epochs, validation_losses, label='Validation Loss')

plt.title('Training and Validation Loss per Epoch')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()