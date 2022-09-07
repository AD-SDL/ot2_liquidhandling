from opentrons import labware, instruments

# Varibales
dna_polymerase_source = 
dna_polymerase_vol =
reaction_buffer_vol  =
reaction_buffer_source = 
dntp_vol =
dntp_source =
gc_enhancer_vol =
gc_enhancer_source =
biowater_vol =
biowater_source = 
master_mix_volume = 30

master_mix_source = 
destination_wells =
pcr_destination_wells = 



# labware #TODO: change specific equipment for use case
#TODO: cooling blocks?
stock_solutions = labware.load('nest_96_wellplate_2ml_deep', '4')
tiprack = labware.load('geb_96_tiprack_10ul', '2')
master_mix = labware.load('nest_96_wellplate_2ml_deep', '5')
pcr_plate = labware.load('nest_96_wellplate_100ul_pcr_full_skirt', '6')
bio_water_stock = labware.load('nest_96_wellplate_2ml_deep', '7')
primers = labware.load('nest_96_wellplate_2ml_deep', '8')
template = labware.load('nest_96_wellplate_2ml_deep', '9')

# TODO: impliment constants instead, convert everything into function

#pipette # TODO: change
pipette = instruments.P10_Single(mount = 'left', tip_racks = [tiprack])

'''
#master mix prep
'''

# biowater # TODO: do math figure out volume needed
pipette.pick_up_tip()
pipette.transfer(biowater_vol, biowater_source, destination_wells, new_tip='always')
pipette.drop_tip()

# dna polymerase
pipette.pick_up_tip()
pipette.transfer(dna_polymerase_vol, dna_polymerase_source, destination_wells, new_tip='always', mix_after=(dna_polymerase_vol))
pipette.drop_tip()

# reaction buffer
pipette.pick_up_tip()
pipette.transfer(reaction_buffer_vol, reaction_buffer_source, destination_wells, new_tip='always', mix_after=(reaction_buffer_vol))
pipette.drop_tip()

# DNTPs
pipette.pick_up_tip()
pipette.transfer(dntp_vol, dntp_source, destination_wells, new_tip='always', mix_after=(dntp_vol))
pipette.drop_tip()

# GC enhancer
pipette.pick_up_tip()
pipette.transfer(gc_enhancer_vol,gc_enhancer_source, destination_wells, new_tip='always', mix_after=(gc_enhancer_vol))
pipette.drop_tip()

'''
# add master mix to PCR plate
'''

pipette.pick_up_tip()
pipette.transfer(master_mix_volume, master_mix_source, pcr_destination_wells, new_tip='never')
pipette.drop_tip()

'''
# add DNA
'''

# TODO: specify location source
# dna template
pipette.pick_up_tip()
pipette.transfer(template_vol, template_source, pcr_destination_wells, new_tip='always', mix_after=(template_vol))
pipette.drop_tip()

# dna primers
pipette.pick_up_tip()
pipette.transfer(primer_vol, primer_source, pcr_destination_wells, new_tip='always', mix_after=(primer_vol))
pipette.drop_tip()