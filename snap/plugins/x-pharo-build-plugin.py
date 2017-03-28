import snapcraft
import shutil
import os

class PharoBuildPlugin(snapcraft.BasePlugin):
	def build(self):
		result = self.run(['mvm'], cwd='build.linux32x86/pharo.cog.spur/build/')
		vmresultsdir = os.path.join(self.builddir, "results")
		shutil.move(vmresultsdir, self.installdir)
		return result
