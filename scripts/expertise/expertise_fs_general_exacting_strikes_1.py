import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'force_sensitive_1a':
		return

	actor.addSkill('expertise_fs_general_exacting_strikes_1')

	actor.addSkillMod('expertise_damage_line_fs_sweep', 2)
	actor.addSkillMod('expertise_damage_line_fs_dm', 2)

	addAbilities(core, actor, player)

	return

def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'force_sensitive_1a':
		return

	actor.removeSkill('expertise_fs_general_exacting_strikes_1')

	actor.removeSkillMod('expertise_damage_line_fs_sweep', 2)
	actor.removeSkillMod('expertise_damage_line_fs_dm', 2)

	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):


	return

def removeAbilities(core, actor, player):


	return
