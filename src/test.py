import blog

print("Terminal color disabled:")
blog.CONFIG_OPTIONS["NO_TERM"] = True

blog.info("info-level")
blog.warn("warn-level")
blog.error("error-level")
blog.debug("debug-level")
blog.web_log("web-level")

print("\n\nTerminal color enabled:")
blog.CONFIG_OPTIONS["NO_TERM"] = False

blog.info("info-level")
blog.warn("warn-level")
blog.error("error-level")
blog.debug("debug-level")
blog.web_log("web-level")

print("\n\n Registering callback test()")

def test(module, loglevel, logmessage):
    print("CALLBACK to test:")
    print(module)
    print(loglevel)
    print(logmessage)

blog.register_output_provider(test)
blog.warn("Test!")
blog.unregister_output_provider(test)

print("enabling debug log..")
blog.enable_debug_level()
blog.debug("debug-level")
blog.disable_debug_level()
