import cmd
class HBNBCommand(cmd.Cmd):
    """ General Class for HBNBCommand """
    prompt = '(hbnb) '

     def do_EOF(self, arg):
        """ Exit method for EOF """
        print('')
        exit()



if __name__ == '__main__':
    HBNBCommand().cmdloop()         
