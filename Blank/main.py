""" 
 Copyright (C) 2018 Claude SIMON (http://q37.info/contact/).

	This file is part of XDHq.

	XDHq is free software: you can redistribute it and/or
	modify it under the terms of the GNU Affero General Public License as
	published by the Free Software Foundation, either version 3 of the
	License, or (at your option) any later version.

	XDHq is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
	Affero General Public License for more details.

	You should have received a copy of the GNU Affero General Public License
	along with XDHq If not, see <http://www.gnu.org/licenses/>.
 """

import os, sys

if not "EPEIOS_SRV" in os.environ:
	sys.path.append("Atlas.python.zip")

import Atlas

def readAsset(path):
	return Atlas.readAsset(path, "blank")

class Blank(Atlas.DOM):
	def __init__(this):
		Atlas.DOM.__init__(this)

	def _acConnect(this,dom,id):
		dom.setLayout("", readAsset("Main.html"))
		dom.addClass("Input","hidden")

	def _acShowInput(this,dom,id):
		dom.removeClass("Input", "hidden")
		dom.focus("Pattern")

	_callbacks = {
		"Connect": _acConnect,
		"Submit": lambda this, dom, id: dom.setContent("Pattern", dom.getContent("Pattern").upper() ),
		"HideInput": lambda this, dom, id: dom.addClass("Input", "hidden"),
		"ShowInput": _acShowInput,
	}
		
	def handle(this,dom,action,id):
		this._callbacks[action](this,dom,id)

Atlas.launch("Connect", readAsset("Head.html"), Blank, "blank")