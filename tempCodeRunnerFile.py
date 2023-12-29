            self.global_vars.tipo = 1
                                        else:
                                            self.global_vars.tipo = 2
                                    else:
                                        self.global_vars.tipo = 3

                                    # Determinando a distância incremental projetada
                                    if self.global_vars.metro == 1:
                                        project = self.project(self.global_vars.Xesq,
                                                           self.global_vars.Xdir,
                                                           self.global_vars.Ysup,
                                                           self.global_vars.Yinf,
                                                           self.global_vars.tipo,