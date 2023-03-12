#
#      Open Source SAM-BA Programmer
#      Released under the MIT license
#
#   dean [at] fourwalledcubicle [dot] com
#         www.fourwalledcubicle.com
#

from . import Part
from . import CortexM0p


class ATSAMD21(CortexM0p):
	"""Part class for all SAMD21 based parts.
	   Note: this will also return true for SAMR21 devices. TODO: fix this.
	"""

	@staticmethod
	def identify(ids):
		"""Determines if the given chip identifiers positively identify a SAMD21
		   series device.

		Args:
			id_name   -- Name of the chip identifier being tested.
			id_values -- Chip identifier values extracted from the part.

		Returns:
			`True` if the given identifiers suggest the part is a SAM D
			series device.
		"""
		
		result = False
		try:
			id_values = ids['DSU']
			result = id_values.processor == 1 and id_values.family == 0 and id_values.series == 1
		except:
			return False
		return result
