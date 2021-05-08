# PartModifier
A Part Modifier for Borderlands 2.

to import, include "from Mods.PartModifier import parts" in your files

# Adding Attributes
addattr()
takes the following 5 inputs in order:

Part Name (use Gibbed SaveEdit for this)

Attribute Name (use https://github.com/BLCM/BLCMods/blob/master/Borderlands%202%20mods/Greem/Resources/BL2/Weapon%20Attributes.txt)

Attribute's Value

Attribute Modifier Type (0=Scale, 1=PreAdd, 2=PostAdd)

Attribute Type (usually just keep this as "AttributeDefinition")

# Actually Executing your changes
writeall() is used to write and execute all changes, add this after all your addattr().

#Notes
As of now I have not implemented a way to delete attributes.

#Contact
Contact me to report bugs 'n things at alexei#2564 on discord
