import bl2sdk
import random
from Mods import PartModifier

class PartModifier(bl2sdk.BL2MOD):
	Name = "PartModifier"
	Description = "Package for modifying the attributes of weapon parts easily."
	Author = "alexei sarov"

instance = PartModifier()

if __name__ == "__main__":
    unrealsdk.Log(f"[{instance.Name}] Manually loaded")
    instance.Enable()
    for mod in ModMenu.Mods:
        if mod.Name == instance.Name:
            if mod.IsEnabled:
                mod.Disable()
            ModMenu.Mods.remove(mod)
            mod.Enable()
            unrealsdk.Log(f"[{instance.Name}] Removed last instance")

            # Fixes inspect.getfile()
            instance.__class__.__module__ = mod.__class__.__module__
            break

bl2sdk.Mods.append(instance)
