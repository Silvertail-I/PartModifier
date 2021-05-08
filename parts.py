import math as m
import unrealsdk
    
allattrs={}

def write(x, y):
    partfile = open("Mods/PartModifier/partchanges.txt", "a")
    partfile.write(f"set {x} WeaponAttributeEffects {y})\n")    #add a line in the file (which will be executed in bl2's command console)
    partfile.close()

def writeall():
    clearfile=open("Mods/PartModifier/partchanges.txt", "w").close()
    for partdef in allattrs:
        write(partdef, allattrs[partdef])
        #unrealsdk.Log(partdef, allattrs[partdef])
    unrealsdk.Log("[PartModifier] All changes written and executed.")
    unrealsdk.GetEngine().GamePlayers[0].Actor.ConsoleCommand("exec Win32/Mods/PartModifier/partchanges.txt", False)

def addattr(part, attr, val, stype, atype): #stype is attribute addition type(when its added) atype is what type of attribute it is (usually AttributeDefinition)
    modifiertypes={"MT_Scale":0, "MT_PreAdd":1, "MT_PostAdd":2}
    if type(stype) == str:
        stype=modifiertypes[stype]
    output={part:""}    #part is the name of the part, the string attatched will be the completed sting of attributes
    oldattrs=str(unrealsdk.FindObject("WeaponPartDefinition", str(part)).WeaponAttributeEffects)   #get all the old attributes
    oldattrs=oldattrs[:-1]     #prune the edges
    oldattrs=oldattrs.replace("{","(")   #convert {} to ()
    oldattrs=oldattrs.replace("}",")")
    oldattrs=oldattrs.replace("[","(")   #convert [] to ()
    oldattrs=oldattrs.replace("]",")")
    #fix oldattrs string
    oldattrs=oldattrs.replace(", ModifierType: ","',ModifierType=")
    oldattrs=oldattrs.replace(": ","=")
    oldattrs=oldattrs.replace("AttributeDefinition ", "AttributeDefinition'")
    #
    if not part in allattrs:
        allattrs[part]=oldattrs
    if len(allattrs[part])>1:
        output[part]+=(f", (AttributeToModify={str(atype)}'{str(attr)}',ModifierType={str(stype)},BaseModifierValue=(BaseValueConstant={str(val)},BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000))")
        '''
        if not str(attr) in allattrs[part]:
            output[part]+=(f", (AttributeToModify={str(atype)}'{str(attr)}',ModifierType={str(stype)},BaseModifierValue=(BaseValueConstant={str(val)},BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000))")
        else:
            unrealsdk.Log(f"[PartModifier] Part alread has {str(attr)}.")
        #^^^^^^^^ add new attribute to the end of the part's attribute list
        '''
    else:
        #unrealsdk.Log("[PartModifier] Part contained no previous attributes")
        output[part]=(f"(AttributeToModify={str(atype)}'{str(attr)}',ModifierType={str(stype)},BaseModifierValue=(BaseValueConstant={str(val)},BaseValueAttribute=None,InitializationDefinition=None,BaseValueScaleConstant=1.000000))")
    #output[part]=output[part][:-1] #more pruning
    allattrs[part]+=output[part]
    #write(part, output[part])


#allattrs[part]+=oldattrs