import snapcraft
import shutil
import os

class PharoBuildPlugin(snapcraft.BasePlugin):
	def build(self):
		result = self.run(['scripts/build.sh'])
		vmresultsdir = os.path.join(self.builddir, "results")
		shutil.move(vmresultsdir, self.installdir)
		return result
