# Program: Day 13 - Lab Asset Information Tool
# Purpose: Record and view details of devices in MY OWN lab 
#
# Uses only: variables, input/print, if/elif/else, loops,
#            lists, dictionaries, functions (Day 1 to Day 12).
# No files and no libraries. Data lives in memory while the program runs.

DEVICE_TYPES = ("server", "laptop", "router", "vm", "other")


# ---------- 1. Collecting device details ----------

def ask_text(prompt):
    """Keep asking until the user types something (not empty)."""
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("This field cannot be empty.")


def ask_device_type():
    """Keep asking until the user picks an allowed type."""
    while True:
        value = input(f"Type {DEVICE_TYPES}: ").strip().lower()
        if value in DEVICE_TYPES:
            return value
        print("Please choose one of the listed types.")


def is_valid_ip(text):
    """Return True if text looks like an IPv4 address."""
    parts = text.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if int(part) > 255:
            return False
    return True


def ip_exists(assets, ip):
    """Return True if this IP is already in the inventory."""
    for asset in assets:
        if asset["ip"] == ip:
            return True
    return False


def ask_ip(assets):
    """Ask until the IP is valid and not already used."""
    while True:
        value = input("IP address: ").strip()
        if not is_valid_ip(value):
            print("Invalid IP. Example: 192.168.56.101")
        elif ip_exists(assets, value):
            print("That IP is already in the inventory.")
        else:
            return value


def ask_ports():
    """Ask for ports like 22,80,443 and return a list of integers."""
    text = input("Open ports, comma-separated (Enter for none): ")
    ports = []
    for item in text.split(","):
        item = item.strip()
        if item.isdigit() and int(item) <= 65535:
            number = int(item)
            if number not in ports:
                ports.append(number)
    ports.sort()
    return ports


# ---------- 2. Storing details in dictionaries ----------

def create_asset(assets):
    """Collect details and return ONE asset as a dictionary."""
    asset_id = f"A{len(assets) + 1:03d}"      # A001, A002, A003 ...
    asset = {
        "id": asset_id,
        "name": ask_text("Device name: "),
        "type": ask_device_type(),
        "ip": ask_ip(assets),
        "os": ask_text("Operating system: "),
        "owner": ask_text("Owner: "),
        "ports": ask_ports(),
    }
    return asset


def find_by_name(assets, name):
    """Return the asset with this name, or None if not found."""
    for asset in assets:
        if asset["name"].lower() == name.lower():
            return asset
    return None


# ---------- 3. Displaying asset information ----------

def ports_to_text(ports):
    """Turn [22, 80] into '22, 80' (or 'none')."""
    if len(ports) == 0:
        return "none"
    text = ""
    for port in ports:
        if text != "":
            text = text + ", "
        text = text + str(port)
    return text


def show_asset(asset):
    """Print one asset as a small card."""
    print("-" * 34)
    print(f"ID:     {asset['id']}")
    print(f"Name:   {asset['name']}")
    print(f"Type:   {asset['type']}")
    print(f"IP:     {asset['ip']}")
    print(f"OS:     {asset['os']}")
    print(f"Owner:  {asset['owner']}")
    print(f"Ports:  {ports_to_text(asset['ports'])}")
    print("-" * 34)


def show_table(assets):
    """Print all assets in an aligned table."""
    if len(assets) == 0:
        print("No assets recorded yet.")
        return

    print(f"{'ID':<6}{'Name':<16}{'Type':<9}{'IP':<16}{'Owner':<10}")
    print("-" * 57)
    for a in assets:
        print(f"{a['id']:<6}{a['name']:<16}{a['type']:<9}{a['ip']:<16}{a['owner']:<10}")


def show_summary(assets):
    """Count how many devices of each type (counting pattern, Day 11)."""
    if len(assets) == 0:
        print("No assets recorded yet.")
        return

    counts = {}
    for a in assets:
        counts[a["type"]] = counts.get(a["type"], 0) + 1

    print(f"Total assets: {len(assets)}")
    for device_type, count in counts.items():
        print(f"  {device_type:<8}{count}")


# ---------- 4. Saving basic asset records ----------
# Without files, "saving" means keeping each record in the `assets` list
# (a list of dictionaries). The records stay available while the program
# is running. Saving to a file comes in later lessons (Day 14 and 15).

def show_menu():
    print()
    print("=" * 34)
    print("  LAB ASSET INFORMATION TOOL")
    print("=" * 34)
    print("1. Add asset")
    print("2. List all assets")
    print("3. View one asset")
    print("4. Summary")
    print("5. Quit")


def main():
    assets = []          # the inventory: a list of dictionaries

    while True:
        show_menu()
        choice = input("Choose 1-5: ").strip()

        if choice == "1":
            asset = create_asset(assets)
            assets.append(asset)                  # "save" the record
            print(f"Saved {asset['name']} as {asset['id']}.")
        elif choice == "2":
            show_table(assets)
        elif choice == "3":
            name = ask_text("Device name to find: ")
            asset = find_by_name(assets, name)
            if asset is None:
                print("No device with that name.")
            else:
                show_asset(asset)
        elif choice == "4":
            show_summary(assets)
        elif choice == "5":
            print("Goodbye. (Records are lost when the program closes.)")
            break
        else:
            print("Please enter a number from 1 to 5.")


main()