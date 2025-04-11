def calculate_real_size(microscope_size, magnification):
    return microscope_size / magnification

if __name__ == "__main__":
    specimen_name = input("Enter specimen name: ")
    microscope_size = float(input("Enter microscope size (in mm): "))
    magnification = float(input("Enter magnification used: "))

    actual_size = calculate_real_size(microscope_size, magnification)
    print(f"Actual size of {specimen_name}: {actual_size:.4f} mm")