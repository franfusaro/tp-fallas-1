from engine.base_de_conocimietos_enfermedades import ConocimientoMedico
import six

class InferenceEngine:

    def __init__(self):
        self.FORWARD = "forward"
        self.BACKWARD = "backward"

        self.__knowledgeBase = ConocimientoMedico()
        self.__clauseBase = None
        self.__verbose = None
        self.__method = None

    def startEngine(self, userInput, method="forward"):
        self.__knowledgeBase = ConocimientoMedico()
        self.__method = method or self.FORWARD
        return self.__inferenceResolve(userInput)

    def __inferenceResolve(self, userInput):

        # run inference with selected method
        if self.__method == "forward":
            return self.__runForwardChain(userInput)
        else:
            return self.__runBackwardChain(userInput)

    def __runForwardChain(self, userBase):

        matchesRules = dict()
        for d in self.__knowledgeBase.diagnosticos:
            matchesRules[d] = []
        # getting each knowledge from the base
        for rule in self.__knowledgeBase.reglas:
            match = 0
            diagnostico = rule['diagnostico']
            # comparing each rule
            for sympthom in self.__knowledgeBase.sintomas:
                if rule['sintomas'][sympthom] == userBase[sympthom]:
                    match += 1

            # adding the percent of match for each target
            matchesRules[diagnostico] \
                .append(match / len(self.__knowledgeBase.sintomas) * 100)

        # high percentage is returned based on satisfaction of MATCH
        result = ''
        print(matchesRules)
        
        diagnosisDict = dict()
        
        for diagnosis in six.iterkeys(matchesRules):
            diagnosisDict[diagnosis] = round(max(matchesRules[diagnosis]))
    
        diagnosis = max(diagnosisDict, key=diagnosisDict.get)
        if diagnosisDict[diagnosis] == 100:
            result = 'El diagnostico es ' + diagnosis
        else:
            result = 'No encontramos un diagnostico que coincida completamente, pero el que más se asemeja es ' + diagnosis + ' con un ' + str(diagnosisDict[diagnosis]) + '%'

        print(result)
        return result

    def __runBackwardChain(self, userBase):
        pass
        # """
        # Running forward chaining.Steps are as follows :

        #     1. Scan the Knowledge Base rules with the user rule
        #     2. When match is found, save the Knowledge target as new target
        #     3. Run match on the selected targets
        #     4. Return the output based on the Min percent

        # Parameters
        # ----------
        # userBase : Knowledge
        #     Knowledge object created by parsing the user input

        # Returns
        # -------
        # tuple
        #     bool : True denoting match found; str : formatted target name and percentage
        # """
        # matchedTargets = list()
        # matchesRules = dict()

        # # finding initial target
        # for knowledge in self.__knowledgeBase:
        #     for rule in knowledge.getRules():
        #         for userRule in userBase.getRules():
        #             # rule match target acquired
        #             if rule == userRule:
        #                 matchedTargets.append(knowledge)
        #                 break

        # # running matching on the selected targets
        # for matchedTarget in matchedTargets:
        #     match = 0
        #     for rule in matchedTarget.getRules():
        #         for userRule in userBase.getRules():
        #             if rule == userRule:
        #                 match += 1

        #     # saving the target with its percent match
        #     matchesRules[matchedTarget.getTarget()] = (match / len(matchedTarget.getRules())) * 100

        # # sorting the matched rules by the percentages
        # matchesRules = sortDictionary(matchesRules)

        # if self.__verbose:
        #     for target, percent in matchesRules.items():
        #         Log.d(f"Target :: {target} --->  Matched :: {percent}")
        #     print()

        # # returning the highest matches target if is greater than the MIN
        # for target, percent in matchesRules.items():
        #     if percent >= PERCENT_MATCH:
        #         return True, target + " " + str(percent) + " % sure"
        #     else:
        #         return False, target

